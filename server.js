const express = require("express");
const ytdlp = require("yt-dlp-exec");

const app = express();

app.get("/", (req,res)=>{
res.send("Server Running");
});

app.get("/download", async (req,res)=>{

const url = req.query.url;

if(!url){
return res.send("No URL");
}

try{

const info = await ytdlp(url,{
dumpSingleJson:true
});

res.redirect(info.url);

}catch(err){

res.send("Error");
}

});

const PORT = process.env.PORT || 3000;

app.listen(PORT, ()=>{
console.log("Running");
});