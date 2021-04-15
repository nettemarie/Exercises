// ES5 Global Constants
// var PI = 3.14;
// PI = 42; // stop me from doing this!

// ES2015 Global Constants
/* Write an ES2015 Version */

let PI = 3.14
PI = 42

// Quiz
// What is the difference between var and let?
// var can be reassigned, redeclared, and mutated. let can be reassigned and mutated but not redeclared. Also, var has function scope while let has block scope.

// What is the difference between var and const?
// Unlike var, const cannot be reassigned or redelcared. However, they both can be mutated. Also, var has function scope while const has block scope.

// What is the difference between let and const?
// const cannot be reassigned or redeclared but it can be mutated. let can be reassigned and mutated but it cannot be redeclared. They both have block scope.

// What is hoisting?
// Variables are lifted or "hoisted" to the top of the scope they are declared in. When using var, you can access the variable name and it's undefined value before it is delcared later. Function declarations are also hoisted and can be invoked "before" they are defined in a codebase. 