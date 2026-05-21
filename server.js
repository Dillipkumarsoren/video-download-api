
const express = require("express");
const ytdlp = require("yt-dlp-exec");

const app = express();

app.get("/", (req,res)=>{
res.send("Server Running");
});

app.get("/download", async (req,res)=>{

const url = req.query.url;

if(!url){

return res.json({
error:"No URL"
});

}

try{

const info = await ytdlp(url,{

dumpSingleJson:true,

format:"best",

extractorArgs:
"youtube:player_client=android_creator",

addHeader:[
"user-agent:com.google.android.youtube/"
]

});

res.json({

title: info.title,

thumbnail: info.thumbnail,

download: info.url

});

}catch(err){

console.log(err);

res.json({
error:"YouTube blocked request"
});

}

});

const PORT =
process.env.PORT || 3000;

app.listen(PORT,()=>{

console.log("Running");

});
