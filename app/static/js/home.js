"use strict";

// hero slider


//  canal next btn
function nextCanalMovie() {
  const onClickButton = document.querySelector(".new_canal");
  const transformItem = document.querySelector(".stream_container");

  nextButton(onClickButton, transformItem, 193);
}
nextCanalMovie();

//  just release next btn

function nextReleaseMovie() {
  const onClickButton = document.querySelector(".next_btn_1");
  const transformItem = document.querySelector(".movies__container_1");

  nextButton(onClickButton, transformItem, 296);
}
nextReleaseMovie();

// movie 2 next btn
function nextPopulerMovie() {
  const onClickButton = document.querySelector(".next_btn_2");
  const transformItem = document.querySelector(".movies__container_2");

  nextButton(onClickButton, transformItem, 366);
}
nextPopulerMovie();
