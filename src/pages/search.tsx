// import data from "../../scrapers/json/course_catalog.json";
import data from "../../scrapers/json/data.json";
import { useRef, useState } from "react";

const search = () => {
  const [filteredData, setFilteredData] = useState([]);

  // const filteredItems = data.filter((item) => {
  //   item.course_id.includes(query.toLowerCase());
  // });

  const handleFilter = (event: any) => {
    const searchWord = event.target.value;
    const newFilter: any = data.filter((value) => {
      return value.course_id.includes(searchWord);
    });
    setFilteredData(newFilter);
  };

  return (
    <div>
      <div>
        <input onChange={handleFilter} type="search" />
      </div>
      <div>
        {filteredData.map((value: any) => {
          return (
            <div>
              {value.department} {value.course_code} {value.class_section_code}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default search;
