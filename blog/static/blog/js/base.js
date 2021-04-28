function toogleResponsiveContainer() {
    if ($(window).width() < 600) {
        $(".content-wrapper").removeClass('main-container');
    } else {
        $(".content-wrapper").addClass('main-container');
    }
}

toogleResponsiveContainer();

$(window).resize(function () {
    toogleResponsiveContainer();
});

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function toogleIcon() {

    var categoriesMenu = document.getElementById("categories-menu");
    if (categoriesMenu.className === "topnav") {
        categoriesMenu.className += " responsive";
    } else {
        categoriesMenu.className = "topnav";
    }

    var menuIcon = document.getElementById("menu-icon");
    if (menuIcon.className.includes("fa-bars")) {
        menuIcon.className = "fa fa-close";
    } else {
        menuIcon.className = "fa fa-bars";
    }

}
