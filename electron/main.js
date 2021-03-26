const {app, BrowserWindow} = require('electron');
const rootHTML = "html/";
const globalShortcut = app.globalShortcut;

function createWindow() {
    const window = new BrowserWindow({
        title: 'Classy',
        icon: 'favicon.ico',
        minWidth: 800, minHeight: 600,
        resizable: true,
    });
    window.autoHideMenuBar = true;
    //window.removeMenu(); // remove the menu bar from the web interface
    //window.loadFile(rootHTML + "index.html");
    window.loadURL("http://localhost:3000/home");

    
    globalShortcut.register("F5", function() {
        console.log("reload window")
		window.reload();
	});
    globalShortcut.register("CommandOrControl+R", function() {
        console.log("reload window")
		window.reload();
	});
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit();
    }
})

app.on('activate', () => {
    if (BrowserWindow.getAllWindows().length === 0) {
        createWindow();
    }
})