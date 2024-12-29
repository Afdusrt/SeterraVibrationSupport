const WebSocket = require('ws');
const { spawn } = require('child_process');
const wss = new WebSocket.Server({ port: 8080 });
wss.on('connection', function connection(ws) {
  ws.on('message', function incoming(message) {
    const data = JSON.parse(message);
    console.log('Received data:', data);
    const duration_ms = data.duration || 1000;
    const scriptPath = 'vibrate-controller.py';
    console.log(`Executing script: ${scriptPath}`);
    const pythonProcess = spawn('python3', [scriptPath, duration_ms.toString()]);
    pythonProcess.stdout.on('data', (data) => {
      console.log(`stdout: ${data}`);
      ws.send(data.toString());
    });
    pythonProcess.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`);
      ws.send(data.toString());
    });
    pythonProcess.on('close', (code) => {
      console.log(`child process exited with code ${code}`);
    });
    pythonProcess.on('error', (error) => {
      console.error(`Error spawning process: ${error.message}`);
      ws.send(`Error spawning process: ${error.message}`);
    });
  });
});
