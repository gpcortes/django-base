const toastCollection = document.getElementsByClassName('toast')
    window.onload = (event) => {
        for (let i = 0; i < toastCollection.length; i++) {
            const toast = new bootstrap.Toast(toastCollection[i])
            toast.show()
        }
    };