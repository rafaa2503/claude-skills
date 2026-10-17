import { Composition } from "remotion";
import { Reel } from "./Reel";
export const Root: React.FC = () => (
  <Composition id="SherkaReel" component={Reel} durationInFrames={720} fps={30} width={1080} height={1920} />
);
