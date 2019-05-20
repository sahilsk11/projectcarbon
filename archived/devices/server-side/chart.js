function generateLineChartObject(lineChartOptions) {
    return {
        type: lineChartOptions['type'], //either generates line graph or bar graph
        data: {
            labels: lineChartOptions['xValues'], //plots time values on x-axis
            datasets: [{
                data: lineChartOptions['yValues'], //plots first dataset y-values
                borderColor: "rgba(0, 0, 0, 0.5)", //sets the line color
                backgroundColor: "rgba(0, 0, 0, 0.1)", //sets the background color
                pointRadius: 1.1, //sets the point size
                type: 'line', //used for testing - ignore
                label: lineChartOptions['yLabel'], //ads the title to the legend
                borderWidth: 1 //sets the line width
            }, {
                data: lineChartOptions['secondDataSet'], //plots the second dataset
                backgroundColor: "rgba(120, 0, 0, 0.7)", //sets the background color
                label: 'Motion Detected', //adds the title to the legdn
                pointRadius: 0 //removes the points
            }]
        },
        options: {
            responsive: true, //fit to container
            maintainAspectRatio: false,
            layout: {
                padding: { //basic spacing
                    top: 20,
                    bottom: 0,
                }
            },
            title: {
                display: false, //don't need a title so this is ignored
                text: '',
                fontSize: 20,
                position: 'top',
            },
            legend: {
                display: lineChartOptions['displayLegend'], //shows the legend
                position: 'top',
                padding: {
                    top: 0
                }
            },
            scales: {
                yAxes: [{
                    scaleLabel: { //adds the y-axis label
                        display: true,
                        labelString: lineChartOptions['yLabel'] 
                    },
                    ticks: { //used for testing, but generated the y-axis step size
                        stepSize: lineChartOptions['suggestedStepSize']
                    }
                }],
                xAxes: [{
                    maxBarThickness: 1.5, //this was used to make the horizontal lines
                    gridLines: {
                        display: lineChartOptions['displayXGridLines'],

                    },
                    scaleLabel: { //i forgot what this is
                        display: true,
                    },
                }]
            }
        }
    }
}