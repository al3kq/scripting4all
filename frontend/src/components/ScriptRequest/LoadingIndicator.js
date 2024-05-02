import styled from 'styled-components';

const LoadingIndicatorWrapper = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
`;

const Spinner = styled.div`
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;

  @keyframes spin {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
`;

const LoadingText = styled.p`
  margin-left: 10px;
  font-size: 18px;
  color: #777;
`;

function LoadingIndicator() {
  return (
    <LoadingIndicatorWrapper>
      <Spinner />
      <LoadingText>Loading...</LoadingText>
    </LoadingIndicatorWrapper>
  );
}

export default LoadingIndicator;