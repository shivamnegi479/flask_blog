/*!
* Start Bootstrap - Clean Blog v6.0.8 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/
window.addEventListener('DOMContentLoaded', () => {
    let scrollPos = 0;
    const mainNav = document.getElementById('mainNav');
    const headerHeight = mainNav.clientHeight;
    window.addEventListener('scroll', function() {
        const currentTop = document.body.getBoundingClientRect().top * -1;
        if ( currentTop < scrollPos) {
            // Scrolling Up
            if (currentTop > 0 && mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-visible');
            } else {
                console.log(123);
                mainNav.classList.remove('is-visible', 'is-fixed');
            }
        } else {
            // Scrolling Down
            mainNav.classList.remove(['is-visible']);
            if (currentTop > headerHeight && !mainNav.classList.contains('is-fixed')) {
                mainNav.classList.add('is-fixed');
            }
        }
        scrollPos = currentTop;
    });
})


let id=document.getElementById('submit')
// 
if ( id != null){

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
}

let jj=window.location.href
if (String(jj).includes("?page")){
    let head=document.getElementsByClassName('masthead')[0]
    window.scrollTo(0, head.offsetHeight)
}
else{
    const pass = () => {}
}