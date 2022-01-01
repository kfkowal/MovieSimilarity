import './App.css';
import {useState, useRef, useEffect} from 'react';
import * as d3 from 'd3';
import axios from 'axios'


function Scatter() {


  
  let [url, setUrl] = useState("http://localhost:8091/?topics=10");

  const handleSubmit = (e)=>{
    e.preventDefault();
    let tmpUrl=`http://localhost:8091/?topics=${numberOfTopics}`;
    console.log(tmpUrl);
    setUrl(tmpUrl);

    console.log("pobrane zostana: ");
    console.log(url);
    axios.get(tmpUrl).then(response =>{
      setProduct(response.data)
    })
    
  }


  const [product, setProduct] = useState(null);
  let [numberOfTopics, setNot] = useState(10);
  const svgRef = useRef();
  let nextModel = false;
  useEffect(()=>{
    
  

        
      

    


    if (product){
      const w = 1000;
      const h=  800;
      const minX = product.minX;
      const minY = product.minY;
      const maxX = product.maxX;
      const maxY = product.maxY;
  
      const svg =d3.select(svgRef.current).attr('width', w).attr('height', h).style('overflow', 'visible').style('margin-top', '100px');
  
  
      const xScale = d3.scaleLinear().domain([minX,maxX]).range([0,w]);
      const yScale = d3.scaleLinear().domain([minY,maxY]).range([h,0]);
  
      svg.selectAll().data(product.coordinates).enter().append('circle')
       .attr('cx', d=> xScale(d[0]))
       .attr('cy', d=> yScale(d[1]))
       .attr('r', 2);
       let tmp=[];

       for (var i = 0; i < product.coordinates.length; i++) {
        tmp.push([product.coordinates[i][0], product.coordinates[i][1], product.titles[i]])
       }
       console.log(tmp[0][2]);

       svg.selectAll("*").remove();
      svg.selectAll().data(tmp).enter().append('text')
       .attr('x', d=> xScale(d[0] ))
       .attr('y', d=> yScale(d[1] ))
       .attr('font-size', '8px')
       .text(d=> d[2]);
       


       svg.call(d3.zoom()
       .extent([[0, 0], [w, h]])
       .scaleExtent([1, 8])
       .on("zoom", zoomed));
  
   function zoomed(e) {
     svg.attr("transform",  e.transform);
   }
  
    }
    


  }, [url, product]);


if (product){
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>Liczba tematów:</label>
        <input type='text' onChange={(e)=>{setNot(e.target.value)}}/>
        <input type='submit' value="Zatwierdz"/>
      </form>
      <svg ref={svgRef}></svg>
    </div>
  );
}
return (
  <div>
      <form onSubmit={handleSubmit}>
        <label>Liczba tematów:</label>
        <input type='text' onChange={(e)=>{
          setNot(e.target.value)}
          }/>
        <input type='submit' value="Zatwierdz"/>
      </form>
  </div>
);
}

export default Scatter;