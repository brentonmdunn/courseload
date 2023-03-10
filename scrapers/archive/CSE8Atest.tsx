import Head from "next/head";

// https://stackoverflow.com/questions/68405235/how-to-pass-a-parameter-in-getstaticprops-in-nextjs

const CSE8Atest = (props: any) => {
  const department = props.department;
  const course_code = props.course_code;

  return (
    <div>
      <h1>CSE 8A</h1>
      <p>
        {department} {course_code}
      </p>
    </div>
  );
};

import fsPromises from "fs/promises";
import path from "path";
export async function getStaticProps() {
  const filePath = path.join(process.cwd(), "scrapers/json/CSE_8A_A00.json");
  const jsonData = await fsPromises.readFile(filePath);
  const objectData = JSON.parse(jsonData.toString());

  return {
    props: objectData,
  };
}

export default CSE8Atest;
