import com.amazonaws.auth.AWSStaticCredentialsProvider;
import com.amazonaws.auth.BasicAWSCredentials;
import com.amazonaws.regions.Regions;
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

        // Obtenha as tags atuais do objeto
        List<Tag> existingTags = getObjectTags(s3Client, bucketName, objectKey);

        // Adicione ou modifique tags conforme necessário
        existingTags.add(new Tag("NovaTag", "ValorDaNovaTag"));

        // Atualize as tags do objeto
        setObjectTags(s3Client, bucketName, objectKey, existingTags);
    }

    private static List<Tag> getObjectTags(AmazonS3 s3Client, String bucketName, String objectKey) {
        GetObjectTaggingRequest getObjectTaggingRequest = new GetObjectTaggingRequest(bucketName, objectKey);
        GetObjectTaggingResponse getObjectTaggingResponse = s3Client.getObjectTagging(getObjectTaggingRequest);
        return getObjectTaggingResponse.getTagSet();
    }

    private static void setObjectTags(AmazonS3 s3Client, String bucketName, String objectKey, List<Tag> newTags) {
        SetObjectTaggingRequest setObjectTaggingRequest = new SetObjectTaggingRequest(
                bucketName,
                objectKey,
                new ObjectTagging(newTags)
        );

        s3Client.setObjectTagging(setObjectTaggingRequest);
    }
}
