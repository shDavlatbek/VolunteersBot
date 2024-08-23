document.addEventListener('DOMContentLoaded', function() {
    const categorySelect = document.querySelector('#id_categories');
    const userSelect = document.querySelector('#id_user');

    categorySelect.addEventListener('change', function() {
        const selectedCategories = Array.from(categorySelect.selectedOptions).map(option => option.value);
        console.log('Selected categories:', selectedCategories);
        console.log('Selected categories:', selectedCategories.join(','));
        
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
