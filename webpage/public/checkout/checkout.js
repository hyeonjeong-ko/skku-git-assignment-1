// Example starter JavaScript for disabling form submissions if there are invalid fields
(() => {
  'use strict'

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll('.needs-validation')
  
  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }
      else{
        window.alert("안드로이드 폰을 구매 하였습니다!");
      }

      form.classList.add('was-validated')
    }, false)
  })
  
})()

function redeemSuccess(){
  window.alert("쿠폰 적용 되었습니다!");
}
