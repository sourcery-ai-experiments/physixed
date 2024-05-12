$(document).ready(function () {
  let isFirstPlotRendered = true;

  $(".input-form").submit(function (event) {
    console.log("Formulier is ingediend!");
    event.preventDefault(); // Voorkom standaardgedrag van formulierinzending

    // Verzamel gegevens uit het formulier
    let formData = $(this).serialize();

    // Stuur formuliergegevens naar de backend met AJAX
    $.ajax({
      type: "POST",
      url: "", // Gebruik huidige URL
      data: formData,
      success: function (data) {
        // Voeg de plot toe aan de container met fade-in animatie alleen bij de eerste keer
        let plotContainer = $(".fig-section");
        if (isFirstPlotRendered) {
          plotContainer.hide().html(data.fig).fadeIn(1000); // 1000 is de duur van de fade-in animatie in milliseconden
          isFirstPlotRendered = false; // Markeer dat de plot al is toegevoegd
        } else {
          plotContainer.html(data.fig); // Voeg de plot toe zonder fade-in animatie
        }
      },
      error: function (xhr, errmsg, err) {
        console.log(xhr.status + ": " + xhr.responseText); // Log eventuele fouten
      },
    });
  });
});
