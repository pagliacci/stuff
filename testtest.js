var foo = {
  createElement: function(tagname) {
    if (this._secretvarthatisneeded) {
      console.log(tagname + " Element Created!");
    }
  },
  _secretvarthatisneeded: true
}

var bar = foo.createElement;
bar("bar");
