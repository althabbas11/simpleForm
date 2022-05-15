$(document).ready(function () {
    $('#submit').click(function () {
        const name = document.getElementById('name').value;
        const age = document.getElementById('age').value;

        $.ajax(
            {
                url: '',
                type: 'get',
                data: {
                    'name': name,
                    'age': age,
                },
                success: function (response) {
                    $('#result').empty().append(response.result);
                }
            }
        )

    });
});