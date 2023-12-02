
//파이썬 파일 실행

const spawn = require('child_process').spawn;

const result = spawn('python', ['Autoipfs.py']);

result.stdout.on('data', function(data) {
    console.log(data.toString());
});

result.stderr.on('data', function(data) {
    console.log(data.toString());
});

/*
const spawn = require('child_process').spawn;
var name ='helloworld'
const result_02 = spawn('python', ['function_args.py', name, '20']);

result_02.stdout.on('data', (result)=>{
    console.log(result.toString());
});

*/
