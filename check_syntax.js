const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const match = html.match(/<script>\s*(const rootData = [\s\S]*?const app = {)/);
if(match) {
    let script = match[1];
    script = script.replace('const app = {', '');
    try {
        eval(script);
        console.log("Syntax is OK");
    } catch(e) {
        console.error("Syntax Error:", e);
    }
} else {
    console.log("Could not find script block");
}
