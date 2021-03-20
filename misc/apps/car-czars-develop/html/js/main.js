$(document).ready(function () {


    $('#testi-slider').owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        navText: ["<i class='fa fa-chevron-left' aria-hidden='true'></i>", "<i class='fa fa-chevron-right' aria-hidden='true'></i>"],
        dots: false,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            1000: {
                items: 1
            }
        }
    })



    //----------------input field number-------------------//
    var input = document.querySelector("#phone");
    window.intlTelInput(input, {
        //   allowDropdown: false,
        //   autoHideDialCode: false,
        //   autoPlaceholder: "off",
        //   dropdownContainer: document.body,
        //   excludeCountries: ["us"],
        //   formatOnDisplay: false,
        //   geoIpLookup: function(callback) {
        //     $.get("http://ipinfo.io", function() {}, "jsonp").always(function(resp) {
        //       var countryCode = (resp && resp.country) ? resp.country : "";
        //       callback(countryCode);
        //     });
        //   },
        //   hiddenInput: "full_number",
        //   initialCountry: "auto",
        //   localizedCountries: { 'de': 'Deutschland' },
        //   nationalMode: false,
        //   onlyCountries: ['us', 'gb', 'ch', 'ca', 'do'],
        //   placeholderNumberType: "MOBILE",
        //   preferredCountries: ['cn', 'jp'],
        //   separateDialCode: true,
        utilsScript: "js/utils.js",
    });



});

jQuery(window).bind('scroll', function () {
    var navHeight = 200 - 70;
    if (jQuery(window).scrollTop() > navHeight) {
        jQuery('.navbar-light').addClass('fixed');
    } else {
        jQuery('.navbar-light').removeClass('fixed');
    }
});





var myDropzone = new Dropzone("div#myId", {
    url: "#"
});

var myDropzone2 = new Dropzone("div#myId2", {
    url: "#"
});