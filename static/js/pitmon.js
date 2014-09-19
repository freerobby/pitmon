var chart = null;

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
    if (chart === null) {
        // Chart never initialized just give up
        return;
    }
    var data = readData();
    d3.select('#plot svg')
        .datum(data)
        .call(chart);
    setTimeout(update_plot, 15000);
}

function create_plot() {
  /*These lines are all chart setup.  Pick and choose which chart features you want to utilize. */
  nv.addGraph(function() {
    chart = nv.models.lineChart()
                  .margin({left: 48})  //Adjust chart margins to give the x-axis some breathing room.
                  .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
                  .transitionDuration(350)  //how fast do you want the lines to transition?
                  .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
                  .showYAxis(true)        //Show the y-axis
                  .showXAxis(true)        //Show the x-axis
    ;

    var data = readData();

    chart.xAxis.tickFormat(function(d) {
        return d3.time.format('%H:%M')(new Date(d))
    });

    chart.yAxis
        .tickFormat(d3.format('.02f'));

    d3.select('#plot svg')
        .datum(data)
        .call(chart);

    //Update the chart when window resizes.
    nv.utils.windowResize(function() { chart.update() });
    return chart;
  });
}

function readData() {
  var series = null;

  $.ajax({
      url: "http://localhost:8000/data",
      type: 'get',
      dataType: 'json',
      async: false,
      success: function(data) {

        var cooktemp = [],
            cookset = [],
            output = [],
            food1temp = [],
            food1set = [],
            food2temp = [],
            food3temp = [];

        for (var i = 0; i < data["cook_temp"].length; i++) {
            ts = data['timestamp'][i]*1000;
            cooktemp.push({x: ts, y:data["cook_temp"][i]})
            cookset.push({x: ts, y:data["cook_set"][i]})
            output.push({x: ts, y:data["output_percent"][i]})
            food1temp.push({x: ts, y:data["food1_temp"][i]})
            food1set.push({x: ts, y:data["food1_set"][i]})
            food2temp.push({x: ts, y:data["food2_temp"][i]})
            food3temp.push({x: ts, y:data["food3_temp"][i]})
        }

        series = [
            {
              values: cooktemp,
              key: "Cook Temp",
              color: '#ff7f0e'
            },
            {
              values: cookset,
              key: "Cook Set",
              color: '#7777ff',
              area: true
            },
            {
              values: output,
              key: "Output Percent",
              color: '#000000'
            },
            {
              values: food1temp,
              key: "Food1 Temp",
              color: '#2ca02c'
            },
            {
              values: food1set,
              key: "Food1 Set",
              color: '#2ca02c',
              area: true
            },
            {
              values: food2temp,
              key: "Food2 Set",
              color: '#2ca02c'
            },
            {
              values: food3temp,
              key: "Food3 Temp",
              color: '#2ca02c'
            }
          ];
      }
  });

  return series;
}

$(document).ready(function() {
  update_data();
  create_plot();
  setTimeout(update_plot, 15000);
});

