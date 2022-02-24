$(document).on("input", "input:file", function () {
  readURL(this);
  document.getElementById("user-img").classList.replace("invisible", "visible");
});
let news_modal = false;

function readURL(input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      $("#user-img").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}
