// import data from "../../scrapers/json/course_catalog.json";
import data from "../../scrapers/json/data.json";

const search = () => {
  return (
    <div>
      <div>
        <input type="text" />
      </div>
      <div>
        {data.map((value, key) => {
          return <div>{value.course_code}</div>;
        })}
      </div>
    </div>
  );
};

export default search;
