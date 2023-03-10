// import data from "../../scrapers/json/course_catalog.json";
import data from "../../scrapers/json/data.json";
import { useRef, useState } from "react";

const Search: React.FC = () => {
  const [filteredData, setFilteredData] = useState([]);

  // const filteredItems = data.filter((item) => {
  //   item.course_id.includes(query.toLowerCase());
  // });

  const handleFilter = (event: any) => {
    const searchWord = event.target.value;
    const newFilter: any = data.filter((value) => {
      return value.course_id
        .toLowerCase()
        .includes(searchWord.toLowerCase().replace(" ", ""));
    });
    setFilteredData(newFilter);
  };

  return (
    <div>
      <div>
        <input onChange={handleFilter} type="search" />
      </div>
      <div className="box">
        {filteredData.map((value: any, key: any) => {
          var colonIdxStart = value.start_time.indexOf(":");
          var colonIdxEnd = value.end_time.indexOf(":");

          var start_time, start_time_num;
          var end_time, end_time_num;

          if (parseInt(value.start_time.substring(0, colonIdxStart)) > 12) {
            start_time_num =
              parseInt(value.start_time.substring(0, colonIdxStart)) - 12;
            start_time =
              start_time_num.toString() +
              value.start_time.substring(colonIdxStart) +
              " PM";
          } else {
            start_time = value.start_time + " AM";
          }

          if (parseInt(value.end_time.substring(0, colonIdxEnd)) > 12) {
            end_time_num =
              parseInt(value.end_time.substring(0, colonIdxEnd)) - 12;
            end_time =
              end_time_num.toString() +
              value.end_time.substring(colonIdxEnd) +
              " PM";
          } else {
            end_time = value.end_time + " AM";
          }

          return (
            <div className="query" key={value.course_id}>
              <p>
                {value.department} {value.course_code}
                {value.class_section_code} | {value.instructor}
              </p>
              <ul>
                <li>
                  Location: {value.building} {value.room}
                </li>
                <li>Days: {value.days}</li>
                <li>
                  Time: {start_time} - {end_time}
                </li>
              </ul>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default Search;
