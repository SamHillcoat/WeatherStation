var chart; // global
    
    /**
 * Request data from the server, add it to the graph and set a timeout 
 * to request again
 */
    function requestData() {
        $.ajax({
            url: 'static/windspeed.json',
            success: function(point) {
                var series = chart.series[0],
                    shift = series.data.length > 20; // shift if the series is 
                                                     // longer than 20

                // add the point
                chart.series[0].addPoint(point, true, shift);

                // call it again after one second
                setTimeout(requestData, 1000);    
            },
            cache: false
        });
    }
    
  $(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'windchart',
            defaultSeriesType: 'spline',
            events: {
                load: requestData
            }
        },
        title: {
            text: 'Windspeed'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            minorGridLineWidth: 0,
            gridLineWidth: 0,
            alternateGridColor: null,
            title: {
                text: 'Speed (Knts)',
                margin: 80
            },
             plotBands: [{ // Light air
                from: 0,
                to: 0.6,
                color: 'rgba(68, 170, 213, 0.1)',
                label: {
                    text: 'Calm',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Light breeze
                from: 0.6,
                to: 6.8,
                color: 'rgba(0, 0, 0, 0)',
                label: {
                    text: 'Light',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Gentle breeze
                from: 6.8,
                to: 10.7,
                color: 'rgba(68, 170, 213, 0.1)',
                label: {
                    text: 'Gentle',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Moderate breeze
                from: 10.7,
                to: 15.6,
                color: 'rgba(0, 0, 0, 0)',
                label: {
                    text: 'Moderate',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Fresh breeze
                from: 15.6,
                to: 21,
                color: 'rgba(68, 170, 213, 0.1)',
                label: {
                    text: 'Fresh',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Strong breeze
                from: 21,
                to: 27,
                color: 'rgba(0, 0, 0, 0)',
                label: {
                    text: 'Strong',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Near Gale
                from: 27,
                to: 33.4,
                color: 'rgba(68, 170, 213, 0.1)',
                label: {
                    text: 'Near Gale',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Gale
                from: 33.4,
                to: 40.4,
                color: 'rgba(0, 0, 0, 0)',
                label: {
                    text: 'Gale',
                    style: {
                        color: '#606060'
                    }
                }
            }, { // Strong Gale
                from: 40.4,
                to: 47.6,
                color: 'rgba(68, 170, 213, 0.1)',
                label: {
                    text: 'Strong Gale',
                    style: {
                        color: '#606060'
                    }

                }}

            ]
        },
        series: [{
            name: 'Windspeed',
            data: [
          
            ]
        }]
    });        
});