const alert = document.getElementById('alert');
const imageBox = document.getElementById('preview');
const form = document.getElementById('p-form');

const name = document.getElementById('id_name');
const desc = document.getElementById('id_desciption');
const image = document.getElementById('id_image');

const itImge = document.getElementById('itImage');

const csrf = document.getElementsByName('csrfmiddlewaretoken');
console.log(csrf)

image.addEventListener('change', ()=>{
    const img_data = image.files[0]
    const url = URL.createObjectURL(img_data)
    console.log(url)

    itImge.src = url;

})

/*

form.addEventListener('submit', e=>{
    e.preventDefault();

    const fd = new FormData()

    fd.append('csrfmiddlewaretoken',csrf[0].value)
    fd.append('name', name.value)
    fd.append('description', desc.value)
    fd.append('image', image.files[0])

    $.ajax({
        type:'POST',
        url:url,
        data:fd,
        success: function(response){
            console.log(response)
        },
        error: function(error){
            console.log(error)
        },
        cache: false,
        contentType: false,
        processData: false,

    })

})

*/