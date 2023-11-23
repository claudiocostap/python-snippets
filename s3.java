import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.*;

import java.util.List;

public class ChangeS3ObjectTag {

    public static void main(String[] args) {
        // Defina as credenciais da AWS
        String accessKey = "SEU_ACCESS_KEY";
        String secretKey = "SEU_SECRET_KEY";

        // Defina o nome do bucket e o caminho do objeto
        String bucketName = "SEU_BUCKET_NAME";
        String objectKey = "SEU_OBJECT_KEY";

        // Crie o cliente S3
        AmazonS3 s3Client = AmazonS3ClientBuilder.standard()
                .withCredentials(new AWSStaticCredentialsProvider(new BasicAWSCredentials(accessKey, secretKey)))
                .withRegion(Regions.US_EAST_1) // Substitua pela sua região
                .build();

        // Obtenha a listagem de objetos
        ListObjectsV2Request listObjectsRequest = new ListObjectsV2Request()
                .withBucketName(bucketName)
                .withPrefix(objectKey);

        ListObjectsV2Response listObjectsResponse = s3Client.listObjectsV2(listObjectsRequest);
        List<S3ObjectSummary> objectSummaries = listObjectsResponse.getObjectSummaries();

        // Verifique se há objetos e obtenha as tags do primeiro objeto
        if (!objectSummaries.isEmpty()) {
            String firstObjectKey = objectSummaries.get(0).getKey();
            GetObjectTaggingRequest getObjectTaggingRequest = new GetObjectTaggingRequest(bucketName, firstObjectKey);
            GetObjectTaggingResponse getObjectTaggingResponse = s3Client.getObjectTagging(getObjectTaggingRequest);
            TagSet tagSet = getObjectTaggingResponse.getTagging();

            // Adicione ou modifique tags conforme necessário
            tagSet.setTag("NovaTag", "ValorDaNovaTag");

            // Atualize as tags do objeto
            SetObjectTaggingRequest setObjectTaggingRequest = new SetObjectTaggingRequest(bucketName, firstObjectKey, tagSet);
            s3Client.setObjectTagging(setObjectTaggingRequest);
        }
    }
}
