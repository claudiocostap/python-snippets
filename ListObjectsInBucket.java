import software.amazon.awssdk.auth.credentials.AwsBasicCredentials;
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.s3.S3Client;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Request;
import software.amazon.awssdk.services.s3.model.ListObjectsV2Response;
import software.amazon.awssdk.services.s3.model.S3Object;
import java.util.List;

public class ListObjectsInBucket {

    public static void main(String[] args) {
        // Defina as credenciais da AWS
        String accessKey = "SEU_ACCESS_KEY";
        String secretKey = "SEU_SECRET_KEY";

        // Defina o nome do bucket
        String bucketName = "SEU_BUCKET_NAME";

        // Crie o cliente S3
        S3Client s3Client = S3Client.builder()
                .region(Region.US_EAST_1) // Substitua pela sua região
                .credentialsProvider(() -> AwsBasicCredentials.create(accessKey, secretKey))
                .build();

        // Liste os objetos no bucket
        listObjects(s3Client, bucketName);
    }

    private static void listObjects(S3Client s3Client, String bucketName) {
        ListObjectsV2Request listObjectsRequest = ListObjectsV2Request.builder()
                .bucket(bucketName)
                .build();

        ListObjectsV2Response listObjectsResponse = s3Client.listObjectsV2(listObjectsRequest);
        List<S3Object> objects = listObjectsResponse.contents();

        // Exiba os objetos
        System.out.println("Objetos no bucket " + bucketName + ":");
        for (S3Object object : objects) {
            System.out.println("Nome do Objeto: " + object.key());
            System.out.println("Tamanho do Objeto: " + object.size());
            System.out.println("Última Modificação: " + object.lastModified());
            System.out.println("--------");
        }
    }
}
