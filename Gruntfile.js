module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    browserify: {
      'build/index.js': ['src/index.js']
    },
  });


  grunt.loadNpmTasks('grunt-browserify');


  grunt.registerTask("default", ["browserify"]);
}

