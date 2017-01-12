# The MIT License (MIT)
#
# Copyright (c) 2016 Leon Jacobs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import click
import numpy
import itertools

from ..utilities import cleanup_wave_data

# Let numpy print full arrays
numpy.set_printoptions(threshold=numpy.nan)


def get_wave_info(wave_file):
    """
        Get Wave File Information

        :param wave_file:
        :return:
    """
    click.secho('Wave File information:')

    click.secho('Audio Channels:            {}'.format(wave_file.getnchannels()), fg='green')
    click.secho('Sample Width (in bytes):   {}'.format(wave_file.getsampwidth()), fg='green')
    click.secho('Sampling Frequency:        {}'.format(wave_file.getframerate()), fg='green')
    click.secho('Number of Audio Frames:    {}'.format(wave_file.getnframes()), fg='green')
    click.secho('Compression Type:          {}'.format(wave_file.getcomptype()), fg='green')
    click.secho('')
    click.secho('Params of get*:            {}'.format(wave_file.getparams()), fg='green')


def get_wave_binary(source):
    """
        Attempt to represent the binary of an OOK wave source.

        The basic idea is to determine the average of all of
        the frame values. Then, determine if the actual value is
        above/below the average and flip the value to a 1/0
        respectively. This is just to cleanup the signal,
        making it easier to work with.

        Next, count how many 1's and 0's there are, average those
        values again, and run a similar function to output 1's and 0's

        NOTE: Large wave files dont work with this as the averages
        are not really useful with that amount of data.

        :param source:
        :return:
    """

    # Read the frames into a numpy array
    signal = numpy.fromstring(source.readframes(-1), dtype=numpy.int16)
    signal = cleanup_wave_data(signal)

    peaks = []
    shortest_peak = float('inf')
    longest_peak = 0
    current_sample_count = 0
    current_bottom_count = 0
    last_sample_value = 0
    bottom_count = "False" #we need bottom count to separate signals, and count should begin after first signal
    signal_id = 0 #to separate signals

    # Attempt to determine the length of the longest & shortest peak
    # by iterating over the cleaned up signal, counting the number
    # of samples before we hit a zero value.
    for (index,), value in numpy.ndenumerate(signal):

        # Zero indicates *no* signal.
        if value == 0:

            # If the last sample value was not zero, it may
            # mean that the previous value had signal and we
            # can go ahead and calculate distances and
            # record the values in the peaks list
            if last_sample_value != 0:
                bottom_count = "True"
                # Check if we still know what the shortest
                # peak was
                if current_sample_count < shortest_peak:
                    shortest_peak = current_sample_count

                # Check if we still know what the longest
                # peak was
                if current_sample_count > longest_peak:
                    longest_peak = current_sample_count

                # Add this peaks data to the peaks list for later processing
                peaks.append({'end_index': index, 'distance': current_sample_count, 'signal_id':signal_id})

            # Null the current sample count as we obviously
            # hit a zero indicating no signal
            if bottom_count == "True":
                current_bottom_count = current_bottom_count + 1 # counter for no signal
            current_sample_count = 0
        else:

            # We have a value, therefore signal, so increment
            # the counter for the number of samples we have
            # processed so far
            if current_bottom_count > 15*shortest_peak:
                signal_id = signal_id + 1
                bottom_count = "False"
                current_bottom_count = 0
            bottom_count = "False"
            current_bottom_count = 0
            current_sample_count += 1
        # Update the last sample value so that the marker
        # for a zero value can process it.
        last_sample_value = value

    # Info
    click.secho('Samples in (Shortest Peak: {}) (Longest Peak: {})'.format(shortest_peak, longest_peak), fg='green')

    # Calculate the Baud rate of PWM
    click.secho('Math for baud rate will be {}/({}/float({}))'.format(1.0, shortest_peak, source.getframerate()))
    sample_rate = int(1.0 / (shortest_peak / float(source.getframerate())))
    click.secho('Source wave file has baud rate of: {}'.format(sample_rate), fg='green')

    # If the shortest peak ends up being one, stop. There nothing
    # of value that can be done here.
    if shortest_peak in [1, float('inf')]:
        click.secho('Can not determine key with a shortest peak of {}.'
                    ' Try re-recording the sample, or shortening it.'.format(shortest_peak), fg='red')
        return

    key = []
    i = 0
    for (peak_index,), peak_data in numpy.ndenumerate(peaks):

        # Calculate how many times the shortest peak fits in the
        # current peak.
        baud_fits_in_peak = peak_data['distance'] // shortest_peak

        # Update the peaks data with the count for this baud
        # fitting
        peaks[peak_index]['baud_fit'] = baud_fits_in_peak

        if baud_fits_in_peak == 1:
            key.append({'value':0, 'signal_id':peaks[peak_index]["signal_id"]})
        else:
            key.append({'value':1, 'signal_id':peaks[peak_index]["signal_id"]})

    # Print the keys we have found!
    if len(key) > 0:
        rangeCap = max([x['signal_id'] for x in key])
        print(rangeCap)
        result = []
        for i in range(rangeCap):
            word = []
            for x in (y for y in key if y['signal_id'] == i):
                word.append(x['value'])
            result.append(word)
        for b in range(len(result)):
            print ("Signal " + str(b) + ": " + str(result[b]))
        #now we need to find dublicates
        same_signal_list = []
        #q = itertools.combinations(result, 2)
        q = list(set(tuple(x) for x,y in itertools.combinations(result, 2) if not cmp(x,y)))
        for non_unique_signal in q:
            non_unique_signal_position = [i for i,x in enumerate(result) if tuple(x)==non_unique_signal]
            print ("non-unique signal " + str(non_unique_signal) + " on position " + str(non_unique_signal_position))
        #for i in q:
        #    if cmp(i[0],i[1])==0:  #same signals
        #        same_signal_list.append(i[0])
        #        print ("non-unique signal" + str(i[0]))
        #print (same_signal_list)
