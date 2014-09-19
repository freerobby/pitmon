function update_data() {
    $.getJSON(
        "http://localhost:8000/current",
        function(data) {

            if (data["DATE"] === undefined) {
                $("#pitmon_status").html("OFFLINE");
                $("#pitmon_status").removeClass();
                $("#pitmon_status").addClass("ERROR");
                return;
            }

            $("#pitmon_status").html("ONLINE");
            $("#pitmon_status").removeClass();
            $("#pitmon_status").addClass("OK");
            $("#pitmon_time").html(data["DATE"] + " " + data["TIME"]);

            $("#cook_name").html(data["COOK_NAME"]);
            $("#cook_status").html(data["COOK_STATUS"]);
            $("#cook_status").removeClass();
            $("#cook_status").addClass(data["COOK_STATUS"]);
            if (data["COOK_STATUS"] != "NO PROBE") {
                $("#cook_temp").html(data["COOK_TEMP"]);
            } else {
                $("#cook_temp").html("n/a");
            }
            $("#cook_set").html(data["COOK_SET"]);
            $("#output_percent").html(data["OUTPUT_PERCENT"]);

            $("#food1_name").html(data["FOOD1_NAME"]);
            $("#food1_status").html(data["FOOD1_STATUS"]);
            $("#food1_status").removeClass();
            $("#food1_status").addClass(data["FOOD1_STATUS"]);
            if (data["FOOD1_STATUS"] != "NO PROBE") {
                $("#food1_temp").html(data["FOOD1_TEMP"]);
            } else {
                $("#food1_temp").html("n/a");
            }
            $("#food1_temp").html(data["FOOD1_TEMP"]);
            $("#food1_set").html(data["FOOD1_SET"]);

            $("#food2_name").html(data["FOOD2_NAME"]);
            $("#food2_status").html(data["FOOD2_STATUS"]);
            $("#food2_status").removeClass();
            $("#food2_status").addClass(data["FOOD2_STATUS"]);
            if (data["FOOD2_STATUS"] != "NO PROBE") {
                $("#food2_temp").html(data["FOOD2_TEMP"]);
            } else {
                $("#food2_temp").html("n/a");
            }
            $("#food2_temp").html(data["FOOD2_TEMP"]);
            $("#food2_set").html(data["FOOD2_SET"]);

            $("#food3_name").html(data["FOOD3_NAME"]);
            $("#food3_status").html(data["FOOD3_STATUS"]);
            $("#food3_status").removeClass();
            $("#food3_status").addClass(data["FOOD3_STATUS"]);
            if (data["FOOD3_STATUS"] != "NO PROBE") {
                $("#food3_temp").html(data["FOOD3_TEMP"]);
            } else {
                $("#food3_temp").html("n/a");
            }
            $("#food3_set").html(data["FOOD3_SET"]);
        }
    ) .fail(function() {
        $("#pitmon_status").html("OFFLINE");
        $("#pitmon_status").removeClass();
        $("#pitmon_status").addClass("ERROR");
    });
    setTimeout(update_data,1000);
}

function update_plot() {
    console.log("plot");
    $("#plot").attr("src", "/plot?ts=" + new Date().getTime());
    setTimeout(update_plot, 5000);
}

$(document).ready(function() {
  update_data();
  update_plot();
});
