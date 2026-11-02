console.log("=== Silahkan Pilih Menu")
console.log("1 - ayam")
console.log("2 - bakso")
console.log("3 - Mie")

let menu = ['ayam', 'bakso', 'mie']



    const form = document.getElementById('form')
    
    form.addEventListener('submit', (e) => {
        e.preventDefault()
        let pesanan = document.getElementById('pesanan').value
        let jumlah = document.getElementById('jumlah').value

        const cetak = document.getElementById('cetak')
        const nota = document.getElementById('nota')

        harga = 0;
    
        if (pesanan == 'ayam'){
            harga = 10000
        }else if(pesanan == 'bakso'){
            harga = 15000
        }else if(pesanan == 'mie'){
            harga = 5000
        }else{
            console.log('anda tidak memesan apapun')
        }
    
        let total = harga * jumlah;

        let totalRupiah = new Intl.NumberFormat('id-ID', {
            style: 'currency',
            currency:'IDR'
        }).format(total)

       cetak.innerHTML = `Anda memesan <strong>${pesanan}</strong> dengan jumlah <strong>${jumlah}</strong> Total harga:<strong>${totalRupiah}</strong>`;
        
    })
    
