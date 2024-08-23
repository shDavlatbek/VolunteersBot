document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.querySelector('#id_categories');
    const userSelect = document.querySelector('#id_user');

    const checkBoxes = categorySelect.querySelectorAll('input[type="checkbox"]');

    checkBoxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            let selectedCategories = Array.from(checkBoxes)
                .filter(checkbox => checkbox.checked)
                .map(checkbox => checkbox.value);
            
            if (selectedCategories.length > 0) {
                // Make an AJAX call to fetch users based on selected categories
                fetch(`/helper/get_users_by_category/?categories=${selectedCategories.join(', ')}`)
                    .then(response => response.json())
                    .then(data => {
                        // Clear the existing options
                        userSelect.innerHTML = '';
                        const userSelectTo = document.getElementById('id_user_to');
                        // Populate the user select field with new options
                        data.users.forEach(user => {
                            const option = document.createElement('option');
                            option.value = user.id;
                            option.text = user.name;

                            const isOptionInUserSelectTo = Array.from(userSelectTo.options).some(opt => opt.value === option.value);

                            if (!isOptionInUserSelectTo) {
                                userSelect.add(option);
                            }
                        });
                        // Reinitialize the Select2 widget
                        // $(userSelect).trigger('change');
                    });
            }else{
                fetch(`/helper/get_users_all`)
                    .then(response => response.json())
                    .then(data => {
                        // Clear the existing options
                        userSelect.innerHTML = '';
                        const userSelectTo = document.getElementById('id_user_to');
                        // Populate the user select field with new options
                        data.users.forEach(user => {
                            const option = document.createElement('option');
                            option.value = user.id;
                            option.text = user.name;

                            const isOptionInUserSelectTo = Array.from(userSelectTo.options).some(opt => opt.value === option.value);

                            if (!isOptionInUserSelectTo) {
                                userSelect.add(option);
                            }
                        });
                        // Reinitialize the Select2 widget
                        // $(userSelect).trigger('change');
                    });
            }
        });
    });

    // userSelect.addEventListener('change', function() {
    //     checkBoxes.forEach(checkbox => {
    //         checkbox.checked = false;
    //         $(userSelect).trigger('change');
    //     });
    // });

    function waitForElement(selector, callback) {
        var interval = setInterval(function() {
            var element = document.querySelector(selector);
            if (element) {
                clearInterval(interval);
                callback(element);
            }
        }, 100); 
    }

    waitForElement('#id_user_add_all_link', function() {
        const userAddAllLink = document.querySelector('#id_user_add_all_link');
        userAddAllLink.addEventListener('click', function (event) {
            checkBoxes.forEach(checkbox => {
                checkbox.checked = false;
            })
        })
    });
});
