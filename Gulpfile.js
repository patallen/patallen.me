var gulp = require('gulp');
var sass = require('gulp-sass');
var autoprefixer = require('gulp-autoprefixer');
//var bower = require('gulp-bower');
var livereload = require('gulp-livereload');

gulp.task('styles', function(){
    gulp.src('app/static/sass/**/*.sass')
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer('last 2 version'))
        .pipe(gulp.dest('static/css/'))
		.pipe(livereload());
});
//gulp.task('bower', function(){
//	return bower()
//		.pipe(gulp.dest('static/components'))
//});

gulp.task('watch', function(){
	livereload.listen();
    gulp.watch('app/static/sass/**/*.sass', ['styles']);
});

gulp.task('default', ['styles', 'watch'], function(){
   // Perform bower and styles then watch server 
});
