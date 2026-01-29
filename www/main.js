$(document).ready(function(){
    $('.text').textillate({
        loop : true,
        sync : true,
        in : {
            effect : "bounceIn"
        },
        out : {
            effect : "bounceOut"
        }
    });
    //Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width : 800,
        height : 200,
        style : "ios9",
        amplitude : "1",
        speed : "0.30",
        autostart : true
    });
    //Siri Message Animation
    $('.siri-message').textillate({
        loop : true,
        sync : true,
        in : {
            effect : "fadeInUp",
            sync : true
        },
        out : {
            effect : "fadeOutUp",
            sync : true
        }
    });
    //Mic Button Click Event
    $("#MicBtn").click(function () {
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#siriwave").attr("hidden", false);
        eel.allCommands()()
    });
    //Short-cut key for mic activation
    function doc_keyUP(e){
        if(e.key === 'y' && e.metaKey){
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUP, false);
    //
    function playAssistant(message){
        if(message != ""){
            $("#Oval").attr("hidden", true);
            $("#siriwave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }
    }
    //show send button when typed in chatbox
    function ShowHideButton(message){
        if(message.length == 0){
            $("#MicBtn").attr("hidden", false);
            $("#SendBtn").attr("hidden", true);
        }else{
            $("#MicBtn").attr("hidden", true);
            $("#SendBtn").attr("hidden", false);
        }
    }
    // If user presses Enter
    $("#chatbox").keyup(function(e){
        let message = $("#chatbox").val();
        ShowHideButton(message);
        if(e.key === "Enter" && message.trim() !== ""){
            playAssistant(message);
        }
    });
    // Or bind to Send button
    $("#SendBtn").click(function(){
        let message = $("#chatbox").val().trim();
        if(message !== ""){
            playAssistant(message);
        }
    });
});