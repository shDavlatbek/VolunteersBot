document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.querySelector('#id_categories');
    const userSelect = document.querySelector('#id_user');


    function waitForElement(selector, callback) {
        var interval = setInterval(function() {
            var element = document.querySelector(selector);
            if (element) {
                clearInterval(interval);
                callback(element);
            }
        }, 100); // Check every 100 milliseconds
    }
    
    
    waitForElement('#id_categories_add_link', function() {
        
        const categorySelectFrom = document.querySelector('#id_categories_from');
        const categorySelectTo = document.querySelector('#id_categories_to');
        const categoryAddLink = document.querySelector('#id_categories_add_link');
        const categoryRemoveLink = document.querySelector('#id_categories_remove_link');
        const userSelect = document.querySelector('#id_user');
    
        categoryAddLink.addEventListener('click', function() {
            const selectedCategories = Array.from(categorySelect.selectedOptions).map(option => option.value);
            console.log(selectedCategories);
            
            if (selectedCategories.length > 0) {
                // Make an AJAX call to fetch users based on selected categories
                fetch(`/helper/get_users_by_category/?categories=${selectedCategories.join(',')}`)
                    .then(response => response.json())
                    .then(data => {
                        // Clear the existing options
                        userSelect.innerHTML = '';
                        console.log(data);
                        
                        // Populate the user select field with new options
                        data.users.forEach(user => {
                            const option = document.createElement('option');
                            option.value = user.id;
                            option.text = user.name;
                            userSelect.add(option);
                        });
    
                        // Reinitialize the Select2 widget
                        $(userSelect).trigger('change');
                    });
            }
        });
    });
    

    // categorySelect.addEventListener('change', function() {
    //     const selectedCategories = Array.from(categorySelect.selectedOptions).map(option => option.value);
        
    //     if (selectedCategories.length > 0) {
    //         // Make an AJAX call to fetch users based on selected categories
    //         fetch(`/helper/get_users_by_category/?categories=${selectedCategories.join(',')}`)
    //             .then(response => response.json())
    //             .then(data => {
    //                 // Clear the existing options
    //                 userSelect.innerHTML = '';
                    
    //                 // Populate the user select field with new options
    //                 data.users.forEach(user => {
    //                     const option = document.createElement('option');
    //                     option.value = user.id;
    //                     option.text = user.name;
    //                     userSelect.add(option);
    //                 });

    //                 // Reinitialize the Select2 widget
    //                 $(userSelect).trigger('change');
    //             });
    //     }
    // });
});
