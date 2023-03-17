// $(document).ready(function () {
//    $('#mbti').on('click',function() { //클릭시 발생
//       let currentclass = document.querySelector("#mbti_disc").classList.value; //id값이 bodymain인
//          if(currentclass='mbti_disc_on'){
//             let teamclass = document.querySelector("#mbti_disc"); //id값이 bodymain인
//             let newclass = ['mbti_disc_off'] //클래스 안에 클래스명을 넣고

//             teamclass.classList.remove(teamclass.classList); //클래스들을 다 지우고
//             teamclass.classList.add(newclass); //생성된 클래스의 인덱스값을 가져옴
//          }else{
//             let teamclass = document.querySelector("#mbti_disc_off"); //id값이 bodymain인
//             let newclass = ['mbti_disc_on'] //클래스 안에 클래스명을 넣고
   
//             teamclass.classList.remove(teamclass.classList); //클래스들을 다 지우고
//             teamclass.classList.add(newclass); //생성된 클래스의 인덱스값을 가져옴
//          };
//       }
//       )
//    }
// );

// $(document).ready(function () {
//    show_comment();
//     $('#mbti').on('click',function() { //클릭시 발생
//         let currentclass = document.querySelector("#mbti_disc").value;
        
//         let nowclass = document.querySelector("#mbti_disc").classList //현재 class를 nowclass에 저장
//         let classes = ['mbti_disc_off'] //클래스 안에 클래스명들을 넣고
//         let randomClass = classes[Math.floor(Math.random() * classes.length)]; //랜덤돌리고
//         while (randomClass==nowclass) { //똑같은지 확인하고 똑같으면
//            randomClass = classes[Math.floor(Math.random() * classes.length)]; //다시 랜덤돌리고 while로 가서 반복(조건에 맞지 않을때까지)
//         }
//            teamclass.classList.remove(...teamclass.classList); //클래스들을 다 지우고
//            teamclass.classList.add(randomClass); //랜덤으로 생성된 클래스의 인덱스값을 가져옴
//            console.log(randomClass);
//         })
// });




// MBTI 버튼을 누르면 설명이 나온다

//  function click(){
//    let mbti_disc = document.getElementById("mbti_disc");
//    let clicked = 0;
//    console.log(mbti_disc)
//    if(clicked){
//      mbti_disc.className = "mbti_disc1";
//      clicked = 0;
//    }else{
//       mbti_disc.className = "mbti_disc";
//      clicked = 1;
//    }
// }

$(document).ready(function () {
   $("#mbti").on("click", function () {
     var note_id = button.data("noteid");
     $(this)
       .find(".asd")
       .attr("onclick", "update_note('" + note_id + "')");
   });
 });



//  좋아요 기능

