const ProgressBar = ({ progress }) => {
  return (
    <div className="progress-bar">
      <div 
        className="progress" 
        style={{ width: `${progress}%` }}
      >
        {progress}%
      </div>
    </div>
  );
}; 