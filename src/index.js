"use strict";

var md5 = require("md5");

exports.doubleTest = function (x) { return x + x; };
exports.md5myName = function () { return md5.digest_s("Charlie Cheever"); };
exports.foxSay = function (phrase) { alert("What does the fox say?"); alert(phrase); };
