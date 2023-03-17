// 함수의 정의를 하는 곳

//댓글 내용을 DB에 저장
function save_comment() {
  let name = $("#name").val();
  let password = $("#pw").val();
  let comment = $("#message-text").val();

  let formData = new FormData();
  formData.append("name_give", name);
  formData.append("password_give", password);
  formData.append("comment_give", comment);

  fetch("/sbs_comment", { method: "POST", body: formData })
    .then((res) => res.json())
    .then((data) => {
      alert(data["msg"]);
    });
  window.location.reload()
}

// 새로고침되면 자동 실행
$(document).ready(function () {
  show_comment();
});

//댓글 내용을 DB에서 불러와서 보여주기
function show_comment() {
  fetch("/sbs_comment")
    .then((res) => res.json())
    .then((data) => {
        console.log(data);
      let rows = data["result"];
      $("#myo_comment_list").empty();
      rows.forEach((a) => {
        let name = a["name"];
        let comment = a["comment"];

        let temp_html = `  <div class="myo_comment_inlist">
                            <div class="myo_comment_content">
                            <span>${comment} </span>
                            </div>
                            <div class="myo_comment_name">
                            <span>by ${name} </span><br>   
                            </div>
                          </div>
                        `
            ;
        console.log(temp_html);
        $("#myo_comment_list").prepend(temp_html);
      });
    });
}


// ================================================================

 

    // function video_mute_on() {
    //     var video_obj = document.getElementById("video_obj");
    //     video_obj.muted = true;
    // }



// $('#audio-control').click(function(){
//     if( $("#myVideo").prop('muted') ) {
//           $("#myVideo").prop('muted', false);
//           $(this).text('Mute');
//       // or toggle class, style it with a volume icon sprite, change background-position
//     } else {
//       $("#myVideo").prop('muted', true);
//       $(this).text('Unmute');
//     }
// });


// function mute_off() {
//   var video = document.getElementById("Video");
//   video.muted = true;
// }

// function mute_on() {
//   var video = document.getElementById("Video");
//   video.muted = true;
// }



// ================================================================
// 댓글삭제



// 댓글 수정



// 메모 삭제 함수
function delete_note(note_id) {
  let formData = new FormData();
  formData.append("note_id", note_id);
  fetch("/delete_note", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
    });
  window.location.reload();
}

$(document).ready(function () {
  $("#updateNoteModal").on("show.bs.modal", function (event) {
    var button = $(event.relatedTarget);
    var note_id = button.data("noteid");
    $(this)
      .find(".modal-footer button.btn-primary")
      .attr("onclick", "update_note('" + note_id + "')");
  });
});

// 메모 수정 함수
function update_note(note_id) {
  let update_title = $("#update_title").val();
  let update_content = $("#update_content").val();
  let formData = new FormData();
  formData.append("title", update_title);
  formData.append("content", update_content);
  formData.append("note_id", note_id);
  fetch("/update_note", { method: "POST", body: formData })
    .then((response) => response.json())
    .then((data) => {
      alert(data["msg"]);
    });
  window.location.reload();
}