let id=document.getElementById('submit')
id.addEventListener('click',(e)=>{
    let name=document.getElementById('name').value
    let email=document.getElementById('email').value
    let phone=document.getElementById('phone').value
    if ((phone=="") && (name=="") && (email=="")){
        e.preventDefault()
        let newel=document.createElement('p')
        newel.id="new_el"
        newel.innerHTML='Please Enter a valid value'
        if (!newel){

            document.getElementById("contactForm").parentNode.insertBefore(newel,document.getElementById("contactForm"))
        }
    }
    else{
        if (newel){
            delete newel
        }
    }
})