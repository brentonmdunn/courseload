import { useRouter } from "next/router";

const CoursePage = (props: any) => {
  const router = useRouter();
  const { code } = router.query;
  const department = props.department;
  const course_code = props.course_code;

  return (
    <div>
      <h1>Page</h1>
      <h3>aH3</h3>
      <p>This should be the code: {code}</p>
    </div>
  );
};

// import fsPromises from "fs/promises";
// import path from "path";
// export async function getStaticProps() {
//   const filePath = path.join(process.cwd(), "scrapers/json/CSE_8A_A00.json");
//   const jsonData = await fsPromises.readFile(filePath);
//   const objectData = JSON.parse(jsonData.toString());

//   return {
//     props: objectData,
//   };
// }

export default CoursePage;
