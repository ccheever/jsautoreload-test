module.exports = function(grunt) {
  grunt.initConfig({
    
    pkg: grunt.file.readJSON('package.json'),


    react: {
      app: {
        options: {
          extension:    'jsx',  // Default
          ignoreMTime:  false, // Default
        },
        files: {
          'build/jsx': 'src/'
        },
      },
    },

    browserify: {
      all: {
        src: ['src/index.js', 'build/jsx/hello.js'],
        dest: 'build/js/index.js',
        options: {
          transform: ['debowerify']
        },
      }
    },

    copy: {
      main: {
        files: [
          {expand: true, src: ['*.py'], dest: 'build/bin/', cwd: 'src/'},
          {expand: true, src: ['**/*.css'], dest: 'build/css/', cwd: 'src/'},
        ]
      }
    },

    watch: {
      scripts: {
        files: ['src/**/*.js', 'src/**/*.jsx', 'src/**/*.css'],
        tasks: ['react', 'browserify', 'copy'],
        options: {
          livereload: true,
        },
      },
    },


  });


  grunt.loadNpmTasks('grunt-browserify');
  grunt.loadNpmTasks('grunt-react');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-watch');


  grunt.registerTask("default", ["react", "browserify", "copy", "watch"]);
}

