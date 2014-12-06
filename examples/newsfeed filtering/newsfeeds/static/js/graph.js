require(['config'], function() {
    'use strict';

    require([
        'd3'
    ], function(d3) {

        var width = window.innerWidth,
        height = window.innerHeight;

        var color = d3.scale.category20();

        var force = d3.layout.force()
            .charge(-120)
            .linkDistance(30)
            .size([width, height]);

        var zoom = d3.behavior.zoom()
            .scaleExtent([1, 10])
            .on('zoom', zoomed);

        var drag = d3.behavior.drag()
            .origin(function(d) { return d; })
            .on('dragstart', dragstarted)
            .on('drag', dragged)
            .on('dragend', dragended);

        var svg = d3.select('body').append('svg')
            .attr('width', width)
            .attr('height', height)
            .append('g')
            .call(zoom);

        var container = svg.append('g').call(drag);

        d3.json('/socialgraph.json', function(error, graph) {
            force
                .nodes(graph.nodes)
                .links(graph.links)
                .start();

            var link = container.selectAll('.link')
                .data(graph.links)
                .enter().append('line')
                .attr('class', 'link');

            var node = container.selectAll('.node')
                .data(graph.nodes)
                .enter().append('g')
                .attr('class', 'node');
                //.call(force.drag)

            node.append('circle')
                .attr('r', 5)
                .style('fill', function(d) { return color(d.id); });

            node.append('text')
                .attr('dx', 12)
                .attr('dy', '.35em')
                .attr('font-size', '10px')
                .attr('fill', '#222222')
                .text(function(d) { return d.id });

            force.on('tick', function() {
                link.attr('x1', function(d) { return d.source.x; })
                    .attr('y1', function(d) { return d.source.y; })
                    .attr('x2', function(d) { return d.target.x; })
                    .attr('y2', function(d) { return d.target.y; });

                node.attr('transform', function(d) {
                    return 'translate(' + [d.x, d.y] + ')';
                });
            });
        });

        function zoomed() {
            container.attr('transform', 'translate(' + d3.event.translate + ')scale(' + d3.event.scale + ')');
        }

        function dragstarted(d) {
            d3.event.sourceEvent.stopPropagation();
            d3.select(this).classed('dragging', true);
        }

        function dragged(d) {
            d3.select(this).attr('cx', d.x = d3.event.x).attr('cy', d.y = d3.event.y);
        }

        function dragended(d) {
            d3.select(this).classed('dragging', false);
        }
    });
});
