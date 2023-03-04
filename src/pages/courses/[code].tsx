import { useRouter } from "next/router";

const CoursePage = () => {
  const router = useRouter();
  const { code } = router.query;

  return (
    <div>
      <h1>Page</h1>
      <h3>H3</h3>
      <p>This should be the code: {code}</p>
    </div>
  );
};

export default CoursePage;
