#!/usr/bin/node
function add(a, b) {
    a = parseInt(process.argv[2]);
    b = parseInt(process.argv[3]);

    if (isNaN(a) || isNaN(b)) {
        console.log('NaN');
    } else {
        console.log(a + b);
    }
}
add();
