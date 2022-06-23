var svg ;

function drawProgress(end){ 
d3.select("svg").remove() 
  if(svg){
  svg.selectAll("*").remove();
  
}
var wrapper = document.getElementById('radialprogress');
var start = 0;
 
var colours = {
  fill: '#FF0000',
  track: '#555555',
  text: '#00C0FF',
  stroke: '#FFFFFF',
}

var radius = 80;
var border = 12;
var strokeSpacing = 4;
var endAngle = Math.PI * 2;
var formatText = d3.format('.0%');
var boxSize = radius * 2;
var count = end;
var progress = start;
var step = end < start ? -0.01 : 0.01;

//Define the circle
var circle = d3.svg.arc()
  .startAngle(0)
  .innerRadius(radius)
  .outerRadius(radius - border);

//setup SVG wrapper
svg = d3.select(wrapper)
  .append('svg')
  .attr('width', boxSize)
  .attr('height', boxSize);

  
// ADD Group container
var g = svg.append('g')
  .attr('transform', 'translate(' + boxSize / 2 + ',' + boxSize / 2 + ')');

//Setup track
var track = g.append('g').attr('class', 'radial-progress');
track.append('path')
  .attr('fill', colours.track)
  .attr('stroke', colours.stroke)
  .attr('stroke-width', strokeSpacing + 'px')
  .attr('d', circle.endAngle(endAngle));

//Add colour fill
var value = track.append('path')
  .attr('fill', colours.fill)
  .attr('stroke', colours.stroke)
  .attr('stroke-width', strokeSpacing + 'px');

//Add text value
var numberText = track.append('text')
  .attr('fill', colours.text)
  .attr('text-anchor', 'middle')
  .attr('dy', '.5rem'); 

  //update position of endAngle
  value.attr('d', circle.endAngle(endAngle * end));
  //update text value
  numberText.text(formatText(end));
  
}

$('#submitClick').click(function(){
  var val = parseInt($('#percent').val());
   drawProgress(val/100)
})
 
drawProgress(10/100)