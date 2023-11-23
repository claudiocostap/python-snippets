import com.amazonaws.services.s3.AmazonS3;
import com.amazonaws.services.s3.AmazonS3ClientBuilder;
import com.amazonaws.services.s3.model.*;

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

        // Obtenha as tags existentes do objeto
        GetObjectTaggingRequest getObjectTaggingRequest = new GetObjectTaggingRequest(bucketName, objectKey);
        GetObjectTaggingResponse getObjectTaggingResponse = s3Client.getObjectTagging(getObjectTaggingRequest);
        TagSet tagSet = getObjectTaggingResponse.getTagging();

        // Adicione ou modifique tags conforme necessário
        tagSet.setTag("NovaTag", "ValorDaNovaTag");

        // Atualize as tags do objeto
        SetObjectTaggingRequest setObjectTaggingRequest = new SetObjectTaggingRequest(bucketName, objectKey, tagSet);
        s3Client.setObjectTagging(setObjectTaggingRequest);
    }
}
