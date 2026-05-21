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
dumpSingleJson:true,
format:"mp4"
});

if(!info.url){

return res.send("Video fetch failed");

}

res.json({

title: info.title,
thumbnail: info.thumbnail,
download: info.url

});

}catch(err){

console.log(err);

res.send("Download Error");

}

});

const PORT = process.env.PORT || 3000;

app.listen(PORT, ()=>{

console.log("Running");

});