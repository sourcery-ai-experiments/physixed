$(document).ready(function () {
  $("#plotForm").submit(function (event) {
    console.log("Formulier is ingediend!");
    event.preventDefault(); // Voorkom standaardgedrag van formulierinzending

    // Verzamel gegevens uit het formulier
    var formData = $(this).serialize();

    // Stuur formuliergegevens naar de backend met AJAX
    $.ajax({
      type: "POST",
      url: "", // Gebruik huidige URL
      data: formData,
      success: function (data) {
        // Voeg de plot toe aan de container
        $("#plotContainer").html(data.fig);
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText); // Log eventuele fouten
      },
    });
  });
});
